# ``WKInternalsNotes/WKFullScreenWindowController/requestExitFullScreen()``

フルスクリーン退出をマネージャに要求する。

## Objective-C Declaration
```objective-c
- (void)requestExitFullScreen;
```

## Discussion
mac 版は `WebFullScreenManagerProxy` に `requestExitFullScreen` をそのまま転送する。iOS 版は `InFullScreen` でなければ `_exitRequested` を立てて待機し、`InFullScreen` ならマネージャへ要求して `_exitingFullScreen` を立てる。マネージャ不在時は即時終了へフォールバックする。

## References
- [`WKFullScreenWindowController.mm#L631`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L631)
- [`WKFullScreenWindowControllerIOS.mm#L1347`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1347)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
