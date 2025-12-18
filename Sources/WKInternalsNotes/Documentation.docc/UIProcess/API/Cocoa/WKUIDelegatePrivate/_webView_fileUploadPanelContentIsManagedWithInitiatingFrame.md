# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:fileUploadPanelContentIsManagedWithInitiatingFrame:)``

ファイルアップロードパネルの内容が管理対象かを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView fileUploadPanelContentIsManagedWithInitiatingFrame:(WKFrameInfo *)frame;
```

## Discussion
WKContentViewInteraction が `fileUploadPanelDestinationIsManaged:` で呼び出し、保持していた `_frameInfoForFileUploadPanel` を `WKFrameInfo` に変換して渡す。判定後は frame 情報を消費する。

## References
- [`WKUIDelegatePrivate.h#L239`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L239)
- [`WKContentViewInteraction.mm#L9710`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9710)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
