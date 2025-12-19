# ``WKInternalsNotes/WKWebView/_showPasswordViewWithDocumentName(_:passwordHandler:)``

`_showPasswordViewWithDocumentName` を表示する。

## Objective-C Declaration
```objective-c
- (void)_showPasswordViewWithDocumentName:(NSString *)documentName passwordHandler:(void (^)(NSString *))passwordHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewIOS.h#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L127)
- [`WKWebViewIOS.mm#L3560`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L3560)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
