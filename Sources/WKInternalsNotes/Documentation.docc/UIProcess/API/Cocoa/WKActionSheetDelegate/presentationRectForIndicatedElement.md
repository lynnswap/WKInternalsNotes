# ``WKInternalsNotes/WKActionSheetDelegate/presentationRectForIndicatedElement()``

指定要素の提示矩形を返す。

## Objective-C Declaration
```objective-c
- (CGRect)presentationRectForIndicatedElement;
```

## Discussion
`WKActionSheetPresentAtElementRect` の場合に `WKActionSheet` が使用する。`WKActionSheetAssistant` では要素の bounds をホストビュー座標に変換してパディングを付ける。

## References
- [`WKActionSheet.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L99)
- [`WKActionSheetAssistant.mm#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L227)
- [`WKActionSheet.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
