# ``WKInternalsNotes/WKExtendedTextInputTraits/setSelectionColorsToMatchTintColor(_:)``

選択色を `tintColor` に合わせて設定する。

## Objective-C Declaration
```objective-c
- (void)setSelectionColorsToMatchTintColor:(UIColor *)tintColor;
```

## Discussion
`tintColor` が `nil` または `UIColor.systemBlueColor` の場合は各色を `nil` にし、そうでなければ挿入点とハンドルを `tintColor`、ハイライトを `alpha=0.2` の色に設定する。

## References
- [`WKExtendedTextInputTraits.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.h#L68)
- [`WKExtendedTextInputTraits.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKExtendedTextInputTraits.mm#L119)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
