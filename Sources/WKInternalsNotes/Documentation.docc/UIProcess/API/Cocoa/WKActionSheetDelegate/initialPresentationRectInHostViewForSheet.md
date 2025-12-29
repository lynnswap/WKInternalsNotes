# ``WKInternalsNotes/WKActionSheetDelegate/initialPresentationRectInHostViewForSheet()``

初回提示時の基準矩形を返す。

## Objective-C Declaration
```objective-c
- (CGRect)initialPresentationRectInHostViewForSheet;
```

## Discussion
`WKActionSheet` がデフォルトの提示位置として利用する。`WKActionSheetAssistant` ではリクエスト座標をホストビュー座標に変換し、周囲に余白を付けた矩形を返す。

## References
- [`WKActionSheet.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L97)
- [`WKActionSheetAssistant.mm#L238`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L238)
- [`WKActionSheet.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
