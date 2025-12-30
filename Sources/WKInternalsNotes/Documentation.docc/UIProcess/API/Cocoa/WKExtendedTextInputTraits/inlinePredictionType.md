# ``WKInternalsNotes/WKExtendedTextInputTraits/inlinePredictionType``

インライン予測の種類を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) UITextInlinePredictionType inlinePredictionType;
```

## Default Value
初期値は `UITextInlinePredictionTypeDefault`（`HAVE(INLINE_PREDICTIONS)` の場合）。

## Discussion
`restoreDefaultValues` で `UITextInlinePredictionTypeDefault` に戻す。

## References
- [`WKExtendedTextInputTraits.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L45)
- [`WKExtendedTextInputTraits.mm#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L132)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
