#ifndef TTSSDK_NEW_H_INCLUDED
#define TTSSDK_NEW_H_INCLUDED

typedef long long TTSHANDLE;

enum{
    USC_SUCCESS = 0,
    RECEIVING_AUDIO_DATA = 1,//还有语音结果需要接收
    AUDIO_DATA_RECV_DONE = 2,//语音结果全部接收完毕
    SYNTH_PROCESS_ERROR = 3,//错误
};

#if defined MAKING_LIB
	#define DLL_PUBLIC
	#define DLL_LOCAL
#else
	#if defined _WIN32 || defined __CYGWIN__
		#ifdef MAKING_DLL
			#ifdef __GNUC__
				#define DLL_PUBLIC __attribute__((dllexport))
			#else
				#define DLL_PUBLIC __declspec(dllexport) // Note: actually gcc seems to also supports this syntax.
			#endif
		#else
			#ifdef __GNUC__
				#define DLL_PUBLIC __attribute__((dllimport))
			#else
				#define DLL_PUBLIC __declspec(dllimport) // Note: actually gcc seems to also supports this syntax.
			#endif
		#endif
		#define DLL_LOCAL
	#else
		#if __GNUC__ >= 4
			#define DLL_PUBLIC __attribute__ ((visibility("default")))
			#define DLL_LOCAL  __attribute__ ((visibility("hidden")))
		#else
			#define DLL_PUBLIC
			#define DLL_LOCAL
		#endif
	#endif
#endif

#ifdef __cplusplus
extern "C"{
#endif
	DLL_PUBLIC int usc_tts_create_service(TTSHANDLE* handle);
	DLL_PUBLIC int usc_tts_create_service_ext(TTSHANDLE* handle, const char *host, const char *port);
	DLL_PUBLIC int usc_tts_release_service(TTSHANDLE handle); //释放合成接口实例
	DLL_PUBLIC int usc_tts_start_synthesis(TTSHANDLE handle);
	DLL_PUBLIC int usc_tts_stop_synthesis(TTSHANDLE handle); //停止合成
	DLL_PUBLIC int usc_tts_text_put(TTSHANDLE handle, const char * textdata, unsigned int textlen); //上传文本数据进行合成
	DLL_PUBLIC const void* usc_tts_get_result(TTSHANDLE handle, unsigned int* audioLen, int* synthStatus, int* errorCode);//获取合成结果
	DLL_PUBLIC const char* usc_tts_get_option(TTSHANDLE handle, int option_id, int* errorCode);//得到扩展属性
	DLL_PUBLIC const char* usc_tts_get_version(TTSHANDLE handle, int* errorCode);//得到版本号
	DLL_PUBLIC int usc_tts_set_option(TTSHANDLE handle, const char* key, const char* value);
	DLL_PUBLIC int usc_tts_cancel(TTSHANDLE handle);

#ifdef __cplusplus
}
#endif
#endif