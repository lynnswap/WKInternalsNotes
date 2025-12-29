# ``WKInternalsNotes/_WKProcessPoolConfiguration/prewarmsProcessesAutomatically``

自動プロセスプリウォームを有効/無効にする。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL prewarmsProcessesAutomatically WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
既定値は `false`（クライアント未設定時は推奨値にフォールバック）。

## Discussion
setter は `setIsAutomaticProcessWarmingEnabled` を設定し、getter は `isAutomaticProcessWarmingEnabled()` を返す。クライアントが未設定の場合は `clientWouldBenefitFromAutomaticProcessPrewarming` の値が使われる。

## References
- [`_WKProcessPoolConfiguration.mm#L246`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L246)
- [`_WKProcessPoolConfiguration.mm#L251`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L251)
- [`APIProcessPoolConfiguration.h#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIProcessPoolConfiguration.h#L195)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
