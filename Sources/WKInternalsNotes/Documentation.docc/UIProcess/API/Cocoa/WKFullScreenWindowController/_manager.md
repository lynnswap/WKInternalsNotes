# ``WKInternalsNotes/WKFullScreenWindowController/_manager()``

保持中の `WebPageProxy` から `WebFullScreenManagerProxy` を取得して返す。ページが無い場合は `nullptr` を返す。

## Objective-C Declaration
```objective-c
- (WebKit::WebFullScreenManagerProxy *)_manager;
```

## Discussion
mac 版は `_page`、iOS 版は `self._webView _page` を参照して `fullScreenManager()` を返す。ページが破棄済みの場合は `nullptr` となるため、呼び出し側は `nullptr` を許容する前提で扱う。

## References
- [`WKFullScreenWindowController.mm#L919`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L919)
- [`WKFullScreenWindowControllerIOS.mm#L1865`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1865)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
