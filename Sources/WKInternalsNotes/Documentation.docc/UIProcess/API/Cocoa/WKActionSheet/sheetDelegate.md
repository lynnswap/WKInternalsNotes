# ``WKInternalsNotes/WKActionSheet/sheetDelegate``

アクションシートの表示情報を提供する delegate を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, assign) id <WKActionSheetDelegate> sheetDelegate;
```

## Discussion
`presentSheet:` / `presentSheetFromRect:` / `updateSheetPosition` などで、表示位置やホストビューの取得に使用される。

## References
- [`WKActionSheet.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L42)
- [`WKActionSheet.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L97)
- [`WKActionSheet.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L110)
- [`WKActionSheet.mm#L223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L223)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
