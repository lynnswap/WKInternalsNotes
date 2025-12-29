# ``WKInternalsNotes/_WKProcessPoolConfiguration/usesSingleWebProcess``

単一の WebProcess を使うかを制御する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL usesSingleWebProcess WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
既定値は `false`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `usesSingleWebProcess` を直接操作する。

## References
- [`_WKProcessPoolConfiguration.mm#L296`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L296)
- [`_WKProcessPoolConfiguration.mm#L301`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L301)
- [`APIProcessPoolConfiguration.h#L198`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L198)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
