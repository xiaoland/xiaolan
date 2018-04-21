// sample.cpp : Defines the entry point for the console application.


#include <fcntl.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <fstream>
#include <string.h>
#include "../libs/libusc.h"
#include "../libs/appKey.h"
using namespace std;
int asr(int argc, char* argv[]);
int main(int argc, char* argv[])
{
	if (argc < 2) {
		fprintf(stderr, "please choose asr/nlu/tts ! Ths first arg must be asr/nlu/tts ! \n");
		return -1;
	}
	char* service = argv[1];
	
	if (strcmp(service, "asr") == 0)
	{
		if (argc < 2) {
			fprintf(stderr, "Usage asr: sample.exe asr <asr_ans.txt> \n");
			return -1;
		}
		printf("\n语音识别：\n");
		asr(argc, argv);
	}
	else if (strcmp(service, "nlu") == 0)
	{
	}
	else if (strcmp(service, "tts") == 0)
	{
	}
	else
	{
		fprintf(stderr, "please choose asr/nlu/tts ! Ths first arg must be asr/nlu/tts ! \n");
		return -1;	
	}
	return 0;
}

// 语音转文字
int automatic_speech_recognition(USC_HANDLE handle, char* audio_format, char* domain, const char* pcmFileName, const char* resultFileName, bool IsUseNlu = false);

// 语音识别接口
int asr(int argc, char* argv[])
{
	const char * resultFileName = argv[2];

	// 创建识别实例
	USC_HANDLE handle;
	int ret = usc_create_service(&handle);
	if (ret != USC_ASR_OK) {
		fprintf(stderr, "usc_create_service_ext error %d\n", ret);
		return ret;
	}

	// 设置识别AppKey secret
	ret = usc_set_option(handle, USC_OPT_ASR_APP_KEY, USC_ASR_SDK_APP_KEY);
	ret = usc_set_option(handle, USC_OPT_USER_SECRET, USC_ASR_SDK_SECRET_KEY);

	ret = usc_login_service(handle);
	if (ret != USC_ASR_OK) {
		fprintf(stderr, "usc_login_service error %d\n", ret);
		return ret;
	}

	automatic_speech_recognition(handle, AUDIO_FORMAT_PCM_16K, RECOGNITION_FIELD_GENERAL, "../testfile/test1_16k.wav", resultFileName);
	automatic_speech_recognition(handle, AUDIO_FORMAT_PCM_16K, RECOGNITION_FIELD_GENERAL, "../testfile/test2_16k.wav", resultFileName);
	automatic_speech_recognition(handle, AUDIO_FORMAT_PCM_8K, RECOGNITION_FIELD_GENERAL, "../testfile/test3_8k.wav", resultFileName);
	automatic_speech_recognition(handle, AUDIO_FORMAT_PCM_8K, RECOGNITION_FIELD_SONG, "../testfile/test4_8k.wav", resultFileName);

	usc_release_service(handle);

	return ret;
}


/*
audio_format : 语音格式，8k/16k
domain : 领域
pcmFileName : 要识别的音频文件
resultFileName : 识别结果保存文件
*/
int automatic_speech_recognition(USC_HANDLE handle, char* audio_format, char* domain, const char* pcmFileName, const char* resultFileName, bool IsUseNlu)
{
	if (NULL == audio_format || NULL == domain || NULL == pcmFileName || NULL == resultFileName)
	{
		printf("asr params is null!\n");
		return -1;
	}

	int ret;
	std::string result = "";
	char buff[640];

	// 打开结果保存文件(UTF-8)
	FILE* fresult = fopen(resultFileName, "a+");
	if (fresult == NULL) {
		fprintf(stderr, "Cann't Create File %s\n", resultFileName);
		return -2;
	}
	// 打开语音文件(16K/8K 16Bit pcm)
	FILE* fpcm = fopen(pcmFileName, "rb");
	if (fpcm == NULL) {
		fprintf(stderr, "Cann't Open File %s\n", pcmFileName);
		return -3;
	}

	fprintf(stderr, pcmFileName);
	fprintf(fresult, pcmFileName);

	// 设置输入语音的格式
	ret = usc_set_option(handle, USC_OPT_INPUT_AUDIO_FORMAT, audio_format);
	ret = usc_set_option(handle, USC_OPT_RECOGNITION_FIELD, domain);

	// 设置语义参数
	if (IsUseNlu)
		ret = usc_set_option(handle, USC_OPT_NLU_PARAMETER, "filterName=search;returnType=json;");

	ret = usc_start_recognizer(handle);
	if (ret != USC_ASR_OK) {
		fprintf(stderr, "usc_start_recognizer error %d\n", ret);
		goto ASR_OVER;
	}

	while (true){

		int nRead = fread(buff, sizeof(char), sizeof(buff), fpcm);
		if (nRead <= 0) {
			break;
		}
		// 传入语音数据
		ret = usc_feed_buffer(handle, buff, nRead);

		if (ret == USC_RECOGNIZER_PARTIAL_RESULT ||
			ret == USC_RECOGNIZER_SPEAK_END) {

			// 获取中间部分识别结果
			result.append(usc_get_result(handle));
		}
		else if (ret < 0) {

			// 网络出现错误退出
			fprintf(stderr, "usc_feed_buffer error %d\n", ret);
			goto ASR_OVER;
		}
	}

	// 停止语音输入
	ret = usc_stop_recognizer(handle);
	if (ret == 0) {

		// 获取剩余识别结果
		result.append(usc_get_result(handle));
		fprintf(fresult, "\t%s\n", result.c_str());
		fprintf(stderr, "\t%s\n", result.c_str());
	}
	else {
		// 网络出现错误退出
		fprintf(stderr, "usc_stop_recognizer error %d\n", ret);
	}

ASR_OVER:
	fclose(fresult);
	fclose(fpcm);
	return ret;
}


