# ``WKInternalsNotes/WKShareSheetDelegate/shareSheet(_:willShowActivityItems:)``

共有シートの表示前にアクティビティ項目を通知する。

## Objective-C Declaration
```objective-c
- (void)shareSheet:(WKShareSheet *)shareSheet willShowActivityItems:(NSArray *)activityItems;
```

## Discussion
共有 UI を提示する直前に、提示予定のアクティビティ項目が渡される。

## References
- [`WKShareSheet.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.h#L55)
- [`WKShareSheet.mm#L419`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.mm#L419)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
