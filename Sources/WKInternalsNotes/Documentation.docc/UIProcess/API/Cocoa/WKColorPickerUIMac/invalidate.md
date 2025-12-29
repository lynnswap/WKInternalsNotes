# ``WKInternalsNotes/WKColorPickerUIMac/invalidate()``

カラーピッカー UI を破棄する。

## Objective-C Declaration
```objective-c
- (void)invalidate;
```

## Discussion
`WKColorPopoverMac` 実装では popover のビューを除去し、ターゲット/アクションを解除して無効化する。関連参照を `nil` にし、共有 `NSColorPanel` の delegate が自分なら解除して閉じる。

## References
- [`WebColorPickerMac.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.h#L50)
- [`WebColorPickerMac.mm#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.mm#L190)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
