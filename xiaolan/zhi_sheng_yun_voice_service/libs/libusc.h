#ifndef _LIBUSC_H_
#define _LIBUSC_H_


// 语音编码格式
#define AUDIO_FORMAT_PCM_16K         "pcm16k"
#define AUDIO_FORMAT_PCM_8K          "pcm8k"

// 识别领域
#define RECOGNITION_FIELD_GENERAL    "general"
#define RECOGNITION_FIELD_POI        "poi"
#define RECOGNITION_FIELD_SONG       "song"
#define RECOGNITION_FIELD_MEDICAL    "medical"
#define RECOGNITION_FIELD_MOVIETV    "movietv"
#define RECOGNITION_FIELD_FRIDGE	"fridge"

// 状态开关
#define USC_ENABLE					"true"
#define USC_DISABLED				"false"

#define LANGUAGE_ENGLISH             "english"
#define LANGUAGE_CANTONESE           "cantonese"
#define LANGUAGE_CHINESE             "chinese"

enum {
    // 识别正常
    USC_ASR_OK                       = 0,

    // 有结果返回
    USC_RECOGNIZER_PARTIAL_RESULT    = 2,

    // 检测到语音开始
    USC_RECOGNIZER_SPEAK_BEGIN       = 100,

    // 检测到语音结束
    USC_RECOGNIZER_SPEAK_END         = 101,

    // 识别句柄错误
	USC_ASR_NO_HANDLE_INPUT			 = -91138,

	// 参数ID错误
	USC_ASR_INVALID_ID				 = -91151,

	// 参数错误
	USC_ASR_INVALID_PARAMETERS		 = -91152,

	// 语音数据格式错误
	USC_ASR_INVALID_INPUT_DATA		 = -91157,

};


enum {
    // 参数为APP_KEY
    USC_OPT_ASR_APP_KEY              = 9,

    // 参数为用户ID
    USC_OPT_ASRUSER_ID               = 14,

    // 选择识别领域 
    USC_OPT_RECOGNITION_FIELD        = 18,

	//语言选择
	USC_OPT_LANGUAGE_SELECT          = 20,   
	
	USC_OPT_ASR_ENGINE_PARAMETER	 = 104,

	// 设置语义参数
	USC_OPT_NLU_PARAMETER			 = 201,

	// 参数为用户secret
	USC_OPT_USER_SECRET				 = 204,

    // 输入语音编码格式
    USC_OPT_INPUT_AUDIO_FORMAT       = 1001,

	// 识别结果文本中是否使用标点符号
	USC_OPT_PUNCTUATION_ENABLED      = 1002,

	// 语音解码帧字节长度
	USC_OPT_DECODE_FRAME_SIZE        = 1003,

	// 噪音数据过滤
	USC_OPT_NOISE_FILTER			 = 1004,
	
	USC_OPT_RESULT_FORMAT			 = 1006,

	USC_SERVICE_STATUS_SELECT		 = 1015,

};

// 定义识别句柄
typedef long long USC_HANDLE;

#ifdef WIN32
	#ifdef LIBUSC_EXPORTS
		#ifdef JNI_EXPORTS
			#define USC_API
		#else
			#define USC_API extern "C" __declspec(dllexport)
		#endif
	#else
		#define USC_API extern "C" __declspec(dllimport)
	#endif
#else
	#define USC_API extern "C" __attribute__ ((visibility("default")))
#endif


// 创建公有云识别
USC_API int usc_create_service(USC_HANDLE* handle);

// 创建私有云识别
USC_API int usc_create_service_ext(USC_HANDLE* handle, const char* host, const unsigned short port);

// 设置VAD超时时间
USC_API void usc_vad_set_timeout(USC_HANDLE handle, int frontSil,int backSil);

// 登录公有云识别
USC_API int usc_login_service(USC_HANDLE handle);

// 启动
USC_API int usc_start_recognizer(USC_HANDLE handle);

// 停止
USC_API int usc_stop_recognizer(USC_HANDLE handle);

// 进行识别
USC_API int usc_feed_buffer(USC_HANDLE handle, const char* buffer, int len);

// 获得识别结果
USC_API const char* usc_get_result(USC_HANDLE handle);

// 释放识别
USC_API void usc_release_service(USC_HANDLE handle);

// 设置识别参数
USC_API int usc_set_option(USC_HANDLE handle, int option_id, const char* value);

// 设置语音参数 string string
USC_API int usc_set_option_str(USC_HANDLE handle, const char* key, const char* value);

// 设置语义参数 string string
USC_API int usc_set_nlu_option_str(USC_HANDLE handle, const char* key, const char* value);

// 获取SDK 版本号
USC_API const char* usc_get_version();

// 当前语音说话开始位置，单位为毫秒
USC_API int usc_get_result_begin_time(USC_HANDLE handle);

// 当前语音说话停止位置，单位为毫秒
USC_API int usc_get_result_end_time(USC_HANDLE handle);

// 获取识别相关参数
USC_API const char * usc_get_option(USC_HANDLE handle, int option_id);

USC_API void usc_clear_option(USC_HANDLE handle, int option_id);

USC_API int usc_cancel_recognizer(USC_HANDLE handle);

#endif

