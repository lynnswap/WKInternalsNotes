# ``WKInternalsNotes/WKTextFinderClient/willDestroyView(_:)``

ビュー破棄時の後始末を行う。

## Objective-C Declaration
```objective-c
- (void)willDestroyView:(NSView *)view;
```

## Discussion
`_page` から `FindMatchesClient`/`FindClient` を解除し、`_view` を `nil` にする。

## References
- [`WKTextFinderClient.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.h#L41)
- [`WKTextFinderClient.mm#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKTextFinderClient.mm#L191)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
