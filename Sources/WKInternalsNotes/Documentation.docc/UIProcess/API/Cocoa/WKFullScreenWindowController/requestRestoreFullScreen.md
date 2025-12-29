# ``WKInternalsNotes/WKFullScreenWindowController/requestRestoreFullScreen(_:)``

フルスクリーン復帰をマネージャに要求する。

## Objective-C Declaration
```objective-c
- (void)requestRestoreFullScreen:(CompletionHandler<void(bool)>&&)completionHandler;
```

## Discussion
`NotInFullScreen` 以外の状態では `completionHandler(false)` で終了する。`WebPageProxy` があれば `fullscreenMayReturnToInline` を通知し、`WebFullScreenManagerProxy` に `requestRestoreFullScreen` を転送する。マネージャが無い場合は失敗として終了する。

## References
- [`WKFullScreenWindowControllerIOS.mm#L1325`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1325)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
