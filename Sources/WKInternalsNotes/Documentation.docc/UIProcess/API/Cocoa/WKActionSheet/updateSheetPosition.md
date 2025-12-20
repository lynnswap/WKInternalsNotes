# ``WKInternalsNotes/WKActionSheet/updateSheetPosition()``

回転後のシート位置を再調整する。

## Objective-C Declaration
```objective-c
- (void)updateSheetPosition;
```

## Discussion
回転処理が完了するまで待機し、現在の表示スタイルに基づいて `presentationRect` を再計算する。表示領域内に収まる場合は `presentSheetFromRect:` で再表示し、モーダルなビューが保持されている場合は `presentSheet:` で復元する。

## References
- [`WKActionSheet.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L47)
- [`WKActionSheet.mm#L211`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L211)
- [`WKActionSheet.mm#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L220)
- [`WKActionSheet.mm#L223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L223)
- [`WKActionSheet.mm#L230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L230)
- [`WKActionSheet.mm#L232`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L232)
- [`WKActionSheet.mm#L234`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L234)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
