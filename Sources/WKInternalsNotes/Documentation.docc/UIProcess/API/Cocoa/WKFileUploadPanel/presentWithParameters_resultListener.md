# ``WKInternalsNotes/WKFileUploadPanel/presentWithParameters(_:resultListener:)``

ファイルアップロードパネルを表示する。

## Objective-C Declaration
```objective-c
- (void)presentWithParameters:(API::OpenPanelParameters*)parameters resultListener:(WebKit::WebOpenPanelResultListenerProxy*)listener;
```

## Discussion
`OpenPanelParameters` から許可ファイル種別やメディアキャプチャ設定を構成し、カメラまたはドキュメントピッカーを表示する。

## References
- [`WKFileUploadPanel.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.h#L54)
- [`WKFileUploadPanel.mm#L495`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.mm#L495)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
