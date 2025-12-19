# ``WKInternalsNotes/WKUserScript/_initWithSource(_:injectionTime:forMainFrameOnly:includeMatchPatternStrings:excludeMatchPatternStrings:associatedURL:contentWorld:deferRunningUntilNotification:)``

deferRunningUntilNotification を受け取る旧 initializer。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithSource:(NSString *)source injectionTime:(WKUserScriptInjectionTime)injectionTime forMainFrameOnly:(BOOL)forMainFrameOnly includeMatchPatternStrings:(nullable NSArray<NSString *> *)includeMatchPatternStrings excludeMatchPatternStrings:(nullable NSArray<NSString *> *)excludeMatchPatternStrings associatedURL:(nullable NSURL *)associatedURL contentWorld:(nullable WKContentWorld *)contentWorld deferRunningUntilNotification:(BOOL)deferRunningUntilNotification WK_API_DEPRECATED_WITH_REPLACEMENT("-_initWithSource:injectionTime:forMainFrameOnly:includeMatchPatternStrings:excludeMatchPatternStrings:associatedURL:contentWorld:", macos(11.0, 15.4), ios(14.0, 18.4), visionos(1.0, 2.4));
```

## Discussion
実装では `deferRunningUntilNotification` は非対応として `NSParameterAssert` し、新しい initializer に委譲する。

## References
- [`WKUserScriptPrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserScriptPrivate.h#L35)
- [`WKUserScript.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUserScript.mm#L101)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
