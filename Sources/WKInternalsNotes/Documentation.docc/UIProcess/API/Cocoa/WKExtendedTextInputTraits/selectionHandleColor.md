# ``WKInternalsNotes/WKExtendedTextInputTraits/selectionHandleColor``

選択ハンドルの色を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) UIColor *selectionHandleColor;
```

## Default Value
初期値は `nil`。

## Discussion
setter は `_selectionHandleColor` に保存し、getter で返す。`restoreDefaultValues` で `nil` に戻す。

## References
- [`WKExtendedTextInputTraits.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L59)
- [`WKExtendedTextInputTraits.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L85)
- [`WKExtendedTextInputTraits.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L150)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
