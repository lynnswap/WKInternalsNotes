# ``WKInternalsNotes/_WKProcessPoolConfiguration/wirelessContextIdentifier``

ワイヤレスコンテキスト識別子を設定するが、現在は実機向けの stub で実質無効。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSUInteger wirelessContextIdentifier WK_API_DEPRECATED("Use of this API is no longer necessary and can be removed", ios(10.12, 13.0));
```

## Default Value
初期値は `0`（getter は常に `0` を返す）。

## Discussion
`PLATFORM(IOS_FAMILY) && !PLATFORM(IOS_FAMILY_SIMULATOR)` のみでコンパイルされるが、getter は `0` を返し setter は空実装。

## References
- [`_WKProcessPoolConfiguration.mm#L166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L166)
- [`_WKProcessPoolConfiguration.mm#L171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L171)
- [`_WKProcessPoolConfiguration.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.h#L50)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
