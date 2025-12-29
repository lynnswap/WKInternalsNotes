# ``WKInternalsNotes/_WKProcessPoolConfiguration/ignoreSynchronousMessagingTimeoutsForTesting``

同期メッセージのタイムアウトを無視するか（テスト用）を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL ignoreSynchronousMessagingTimeoutsForTesting WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
既定値は `false`。

## Discussion
getter/setter は `ProcessPoolConfiguration` の `ignoreSynchronousMessagingTimeoutsForTesting` に直結する。

## References
- [`_WKProcessPoolConfiguration.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L110)
- [`_WKProcessPoolConfiguration.mm#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L115)
- [`APIProcessPoolConfiguration.h#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L181)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
