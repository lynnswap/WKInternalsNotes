# ``WKInternalsNotes/WKColorPickerUIMac/setAndShowPicker(_:withColor:supportsAlpha:suggestions:)``

カラーピッカーを設定して表示する。

## Objective-C Declaration
```objective-c
- (void)setAndShowPicker:(WebKit::WebColorPickerMac*)picker withColor:(NSColor *)color supportsAlpha:(WebKit::ColorControlSupportsAlpha)supportsAlpha suggestions:(Vector<WebCore::Color>&&)suggestions;
```

## Discussion
`WKColorPopoverMac` 実装では `picker` を保持し、`WKPopoverColorWell` に target/action、色、アルファ対応を設定する。候補色は最大 12 件まで `NSColorList` に詰めて渡し、ポップオーバーを表示する。`NSColorPanel` の delegate を自分に設定し、ユーザー操作フラグを初期化する。

## References
- [`WebColorPickerMac.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.h#L49)
- [`WebColorPickerMac.mm#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.mm#L152)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
