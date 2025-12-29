# ``WKInternalsNotes/WKColorPickerUIMac/setColor(_:)``

カラーピッカーの現在色を更新する。

## Objective-C Declaration
```objective-c
- (void)setColor:(NSColor *)color;
```

## Discussion
`WKColorPopoverMac` 実装では `_lastChangedByUser` を `NO` にしてから `WKPopoverColorWell` の色を更新する。

## References
- [`WebColorPickerMac.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.h#L51)
- [`WebColorPickerMac.mm#L231`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.mm#L231)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
