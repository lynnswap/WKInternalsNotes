# ``WKInternalsNotes/WKUserScript/_initWithSource(_:injectionTime:forMainFrameOnly:includeMatchPatternStrings:excludeMatchPatternStrings:associatedURL:contentWorld:)``

match pattern と content world を指定して user script を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithSource:(NSString *)source injectionTime:(WKUserScriptInjectionTime)injectionTime forMainFrameOnly:(BOOL)forMainFrameOnly includeMatchPatternStrings:(nullable NSArray<NSString *> *)includeMatchPatternStrings excludeMatchPatternStrings:(nullable NSArray<NSString *> *)excludeMatchPatternStrings associatedURL:(nullable NSURL *)associatedURL contentWorld:(nullable WKContentWorld *)contentWorld WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
match pattern、associated URL、注入タイミングを `WebCore::UserScript` に組み立て、content world 未指定時は page content world を使う。

## References
- [`WKUserScriptPrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserScriptPrivate.h#L35)
- [`WKUserScript.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserScript.mm#L109)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
