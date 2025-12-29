# ``WKInternalsNotes/WKActionSheetDelegate/presentationRectForElementUsingClosestIndicatedRect()``

最も近い指示矩形を用いた提示矩形を返す。

## Objective-C Declaration
```objective-c
- (CGRect)presentationRectForElementUsingClosestIndicatedRect;
```

## Discussion
`WKActionSheetPresentAtClosestIndicatorRect` の場合に `WKActionSheet` が使用する。`WKActionSheetAssistant` では TextIndicator の矩形からタップ位置を含む領域を探し、ホストビュー座標に変換して返す。

## References
- [`WKActionSheet.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L102)
- [`WKActionSheetAssistant.mm#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L199)
- [`WKActionSheet.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
