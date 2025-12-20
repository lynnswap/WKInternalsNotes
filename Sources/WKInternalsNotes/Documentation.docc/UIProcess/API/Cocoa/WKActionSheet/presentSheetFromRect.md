# ``WKInternalsNotes/WKActionSheet/presentSheetFromRect(_:)``

指定矩形からアクションシートを表示する。

## Objective-C Declaration
```objective-c
- (BOOL)presentSheetFromRect:(CGRect)presentationRect;
```

## Discussion
`sheetDelegate` から `hostViewForSheet` を取得し、`UIPopoverPresentationController` の `sourceView` / `sourceRect` / `permittedArrowDirections` を設定する。回転中の delegate があれば復元し、`_wk_viewControllerForFullScreenPresentation` から表示する。

## References
- [`WKActionSheet.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L46)
- [`WKActionSheet.mm#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L108)
- [`WKActionSheet.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L110)
- [`WKActionSheet.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L117)
- [`WKActionSheet.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L120)
- [`WKActionSheet.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L125)
- [`WKActionSheet.mm#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L126)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
