# ``WKInternalsNotes/_WKProcessPoolConfiguration/maximumProcessCount``

最大プロセス数を返すが、現在は常に `NSUIntegerMax`。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSUInteger maximumProcessCount WK_API_DEPRECATED("It is no longer possible to limit the number of processes", macos(10.0, 10.15), ios(1.0, 13.0));
```

## Default Value
常に `NSUIntegerMax` を返す。

## Discussion
getter は `NSUIntegerMax` を返し、setter は空実装で値を保持しない（deprecated）。

## References
- [`_WKProcessPoolConfiguration.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L81)
- [`_WKProcessPoolConfiguration.mm#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L87)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
