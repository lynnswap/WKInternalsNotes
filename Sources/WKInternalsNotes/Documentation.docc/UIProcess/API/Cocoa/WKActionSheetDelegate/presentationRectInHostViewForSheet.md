# ``WKInternalsNotes/WKActionSheetDelegate/presentationRectInHostViewForSheet()``

現在の提示矩形を返す。

## Objective-C Declaration
```objective-c
- (CGRect)presentationRectInHostViewForSheet;
```

## Discussion
`WKActionSheetAssistant` では最新の位置情報から矩形を計算し、対象要素外になった場合は要素中央へ補正して返す。

## References
- [`WKActionSheetAssistant.mm#L248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L248)
- [`WKActionSheet.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
