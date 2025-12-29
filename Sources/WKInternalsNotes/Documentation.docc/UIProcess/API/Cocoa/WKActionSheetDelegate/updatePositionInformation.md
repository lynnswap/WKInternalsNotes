# ``WKInternalsNotes/WKActionSheetDelegate/updatePositionInformation()``

位置情報の再取得を要求する。

## Objective-C Declaration
```objective-c
- (void)updatePositionInformation;
```

## Discussion
回転後の再配置時に `WKActionSheet` から呼び出される。`WKActionSheetAssistant` では delegate に `updatePositionInformationForActionSheetAssistant:` を通知する。

## References
- [`WKActionSheet.mm#L241`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L241)
- [`WKActionSheetAssistant.mm#L267`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L267)
- [`WKActionSheet.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L57)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
