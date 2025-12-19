# ``WKInternalsNotes/WKShareSheetDelegate/shareSheetDidDismiss(_:)``

共有シートが閉じたことを通知する。

## Objective-C Declaration
```objective-c
- (void)shareSheetDidDismiss:(WKShareSheet *)shareSheet;
```

## Discussion
`WKShareSheet` の `dismiss` 完了後に呼ばれる。

## References
- [`WKShareSheet.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.h#L54)
- [`WKShareSheet.mm#L476`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKShareSheet.mm#L476)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
