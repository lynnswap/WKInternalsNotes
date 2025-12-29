# ``WKInternalsNotes/_WKProcessPoolConfiguration/configureJSCForTesting``

JSC をテスト用に構成するかどうかを設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL configureJSCForTesting WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
既定値は `false`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `shouldConfigureJSCForTesting` に直結する。

## References
- [`_WKProcessPoolConfiguration.mm#L362`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L362)
- [`_WKProcessPoolConfiguration.mm#L367`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L367)
- [`APIProcessPoolConfiguration.h#L196`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L196)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
