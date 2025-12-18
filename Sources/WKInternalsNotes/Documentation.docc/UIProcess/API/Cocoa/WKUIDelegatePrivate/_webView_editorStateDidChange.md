# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:editorStateDidChange:)``

編集状態の変化を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView editorStateDidChange:(NSDictionary *)editorState WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
WKWebView の `_didChangeEditorState` 内で selection attributes が変化したタイミングに `dictionaryRepresentationForEditorState` の結果を渡す。コメントではテスト用途の API であることが示されている。

## References
- [`WKUIDelegatePrivate.h#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L179)
- [`WKWebView.mm#L2295`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2295)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
