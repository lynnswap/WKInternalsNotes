# ``WKInternalsNotes/WKFullScreenWindowController/enterFullScreen(_:completionHandler:)``

フルスクリーン開始要求を処理し、提示先の `UIWindowScene` を確定して遷移処理へ進む。

## Objective-C Declaration
```objective-c
- (void)enterFullScreen:(CGSize)mediaDimensions completionHandler:(CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
既にフルスクリーン中または `WebPageProxy` が無い場合は `completionHandler(false)` で終了する。`fullscreenClient().requestPresentingViewController` で提示先を取得し、エラーや退出要求があれば即時終了する。提示元から `UIWindowScene` を解決できたら `_enterFullScreen:windowScene:` に進む。

## References
- [`WKFullScreenWindowControllerIOS.mm#L944`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L944)
- [`WKFullScreenWindowControllerIOS.mm#L1015`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1015)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
