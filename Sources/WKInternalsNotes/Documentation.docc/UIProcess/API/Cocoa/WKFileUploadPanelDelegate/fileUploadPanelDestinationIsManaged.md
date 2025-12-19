# ``WKInternalsNotes/WKFileUploadPanelDelegate/fileUploadPanelDestinationIsManaged(_:)``

アップロード先が管理対象かどうかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)fileUploadPanelDestinationIsManaged:(WKFileUploadPanel *)fileUploadPanel;
```

## Discussion
ドキュメントピッカーの管理状態を設定するために参照される。

## References
- [`WKFileUploadPanel.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.h#L71)
- [`WKFileUploadPanel.mm#L860`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/forms/WKFileUploadPanel.mm#L860)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
