# ``WKInternalsNotes/WKExtendedTextInputTraits/insertionPointColor``

挿入点の色を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) UIColor *insertionPointColor;
```

## Default Value
初期値は `nil`。

## Discussion
setter は `_insertionPointColor` に保存し、getter で返す。`restoreDefaultValues` で `nil` に戻す。

## References
- [`WKExtendedTextInputTraits.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L58)
- [`WKExtendedTextInputTraits.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L75)
- [`WKExtendedTextInputTraits.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L149)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
