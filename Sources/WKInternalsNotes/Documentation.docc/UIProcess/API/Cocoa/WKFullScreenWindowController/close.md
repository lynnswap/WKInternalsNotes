# ``WKInternalsNotes/WKFullScreenWindowController/close()``

フルスクリーンを即時終了し、ウィンドウや参照を解放する。

## Objective-C Declaration
```objective-c
- (void)close;
```

## Discussion
mac 版は `exitFullScreenImmediately` で即時終了処理を走らせた後に `NSWindowController` の `close` を実行し、`_webView` を `nil` にする。iOS 版も `_exitFullscreenImmediately` を呼んだうえで `self._webView` を `nil` にし、迅速なクリーンアップを行う。

## References
- [`WKFullScreenWindowController.mm#L809`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L809)
- [`WKFullScreenWindowControllerIOS.mm#L1562`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1562)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
