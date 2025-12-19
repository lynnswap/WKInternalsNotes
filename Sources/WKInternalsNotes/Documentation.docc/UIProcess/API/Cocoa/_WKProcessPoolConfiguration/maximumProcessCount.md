# ``WKInternalsNotes/_WKProcessPoolConfiguration/maximumProcessCount``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSUInteger maximumProcessCount WK_API_DEPRECATED("It is no longer possible to limit the number of processes", macos(10.0, 10.15), ios(1.0, 13.0));
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKProcessPoolConfiguration.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
