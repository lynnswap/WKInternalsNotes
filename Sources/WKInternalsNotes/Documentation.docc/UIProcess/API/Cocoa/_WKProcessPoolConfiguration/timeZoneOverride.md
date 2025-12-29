# ``WKInternalsNotes/_WKProcessPoolConfiguration/timeZoneOverride``

WebProcess のタイムゾーンを上書きする文字列を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSString *timeZoneOverride WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
初期値は空文字列（未設定）。

## Discussion
getter は `WTF::String` を `NSString` に変換して返し、setter は `ProcessPoolConfiguration` に保存する。

## References
- [`_WKProcessPoolConfiguration.mm#L372`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L372)
- [`_WKProcessPoolConfiguration.mm#L377`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L377)
- [`APIProcessPoolConfiguration.h#L214`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L214)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
