# ``WKInternalsNotes/WKFileUploadPanelDelegate/fileUploadPanelDidDismiss(_:)``

パネルの終了を通知する。

## Objective-C Declaration
```objective-c
- (void)fileUploadPanelDidDismiss:(WKFileUploadPanel *)fileUploadPanel;
```

## Discussion
パネルのキャンセルや完了時に `WKFileUploadPanel` から呼ばれる。

## References
- [`WKFileUploadPanel.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.h#L70)
- [`WKFileUploadPanel.mm#L431`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.mm#L431)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
