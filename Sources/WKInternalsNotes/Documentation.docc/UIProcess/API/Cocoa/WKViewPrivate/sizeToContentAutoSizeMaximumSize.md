# ``WKInternalsNotes/WKView/sizeToContentAutoSizeMaximumSize``

サイズ調整時の最大サイズを返す。

## Objective-C Declaration
```objective-c
@property (readwrite) NSSize sizeToContentAutoSizeMaximumSize;
```

## Default Value
`NSZeroSize`。

## Discussion
getter は `{ }` を返し、setter は空実装。

## References
- [`WKViewPrivate.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L61)
- [`WKView.mm#L1056`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKView.mm#L1056)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
