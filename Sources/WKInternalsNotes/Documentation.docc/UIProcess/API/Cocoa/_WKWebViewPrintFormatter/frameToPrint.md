# ``WKInternalsNotes/_WKWebViewPrintFormatter/frameToPrint``

印刷対象のフレームを保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong) _WKFrameHandle *frameToPrint;
```

## Default Value
`nil`。

## Discussion
`_frameToPrint` の getter/setter を提供し、印刷対象フレームを保持する。

## References
- [`_WKWebViewPrintFormatter.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.h#L36)
- [`_WKWebViewPrintFormatter.mm#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L59)
- [`_WKWebViewPrintFormatter.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L64)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
