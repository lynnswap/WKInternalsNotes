# ``WKInternalsNotes/WKExtendedTextInputTraits/selectionHighlightColor``

選択ハイライトの色を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) UIColor *selectionHighlightColor;
```

## Default Value
初期値は `nil`。

## Discussion
setter は `_selectionHighlightColor` に保存し、getter で返す。`restoreDefaultValues` で `nil` に戻す。

## References
- [`WKExtendedTextInputTraits.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L60)
- [`WKExtendedTextInputTraits.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L95)
- [`WKExtendedTextInputTraits.mm#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L151)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
