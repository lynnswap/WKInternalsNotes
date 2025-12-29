# ``WKInternalsNotes/WKPopoverColorWellDelegate/didClosePopover()``

カラーウェルのポップオーバー終了通知。

## Objective-C Declaration
```objective-c
- (void)didClosePopover;
```

## Discussion
`WKPopoverColorWell` がポップオーバー終了時に呼び出す。`WKColorPopoverMac` 実装では、`NSColorPanel` が非表示ならピッカーを終了する。

## References
- [`WebColorPickerMac.mm#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.mm#L54)
- [`WebColorPickerMac.mm#L239`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WebColorPickerMac.mm#L239)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
