# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:startXRSessionWithFeatures:colorFormat:depthFormat:completionHandler:)``

XR セッション開始を delegate に依頼する（features/format 指定）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView startXRSessionWithFeatures:(_WKXRSessionFeatureFlags)features colorFormat:(MTLPixelFormat)pixelFormat depthFormat:(MTLPixelFormat)depthFormat completionHandler:(void (^)(id, UIViewController *))completionHandler WK_API_AVAILABLE(ios(17.4), visionos(1.1));
```

## Discussion
UIClient がセッション feature と Metal の pixel format を渡し、`CompletionHandlerCallChecker` で結果と view controller を受け取る。

## References
- [`WKUIDelegatePrivate.h#L280`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L280)
- [`UIDelegate.mm#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L215)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
