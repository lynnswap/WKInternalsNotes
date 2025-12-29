# ``WKInternalsNotes/_WKProcessPoolConfiguration/shouldCaptureAudioInUIProcess``

UIProcess でのオーディオキャプチャ許可を表すが、現状は設定が反映されない。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldCaptureAudioInUIProcess WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
初期値は `NO`（未設定）。

## Discussion
`_WKProcessPoolConfiguration.mm` に getter/setter 実装が無く、`ProcessPoolConfiguration` への橋渡しが行われない。C API 側の `WKContextConfigurationSetShouldCaptureAudioInUIProcess` も no-op で、設定しても実挙動に影響しない。

## References
- [`_WKProcessPoolConfiguration.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.h#L62)
- [`WKContextConfigurationRef.cpp#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/C/WKContextConfigurationRef.cpp#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
