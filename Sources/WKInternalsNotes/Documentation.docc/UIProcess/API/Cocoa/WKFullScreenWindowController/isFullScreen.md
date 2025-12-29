# ``WKInternalsNotes/WKFullScreenWindowController/isFullScreen``

内部状態に基づいてフルスクリーン中かどうかを返す。

## Objective-C Declaration
```objective-c
@property (readonly, assign, nonatomic) BOOL isFullScreen;
```

## Default Value
初期状態では `NO`。状態フラグの遷移に応じて値が変化する。

## Discussion
mac 版は `WaitingToEnterFullScreen` / `EnteringFullScreen` / `InFullScreen` を `true` とする。iOS 版はさらに `WaitingToExitFullScreen` / `ExitingFullScreen` も `true` として扱い、退出処理中もフルスクリーン扱いとする。

## References
- [`WKFullScreenWindowController.mm#L295`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L295)
- [`WKFullScreenWindowControllerIOS.mm#L900`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L900)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
