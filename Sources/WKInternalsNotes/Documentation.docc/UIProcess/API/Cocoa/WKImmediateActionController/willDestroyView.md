# ``WKInternalsNotes/WKImmediateActionController/willDestroyView(_:)``

ビュー破棄前の後始末を行う。

## Objective-C Declaration
```objective-c
- (void)willDestroyView:(NSView *)view;
```

## Discussion
`_page` / `_view` / `_viewImpl` / `_hitTestResultData` などをクリアし、Quick Look の delegate を解除して `_immediateActionRecognizer` と状態をリセットする。

## References
- [`WKImmediateActionController.h#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKImmediateActionController.h#L81)
- [`WKImmediateActionController.mm#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKImmediateActionController.mm#L79)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
