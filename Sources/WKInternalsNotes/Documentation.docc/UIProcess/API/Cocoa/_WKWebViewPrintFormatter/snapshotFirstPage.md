# ``WKInternalsNotes/_WKWebViewPrintFormatter/snapshotFirstPage``

最初のページをスナップショットとして扱うかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL snapshotFirstPage WK_API_AVAILABLE(ios(11.0));
```

## Default Value
`NO`。

## Discussion
`YES` の場合、`_shouldDrawUsingBitmap` が `NO` を返し、`rectForPageAtIndex:` は `paperRect` を返す挙動になる。

## References
- [`_WKWebViewPrintFormatter.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.h#L37)
- [`_WKWebViewPrintFormatter.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L76)
- [`_WKWebViewPrintFormatter.mm#L166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/_WKWebViewPrintFormatter.mm#L166)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
