# ``WKInternalsNotes/WKProcessPool/_seedResourceLoadStatisticsForTestingWithFirstParty(_:thirdParty:shouldScheduleNotification:completionHandler:)``

ResourceLoadStatistics を指定ドメインでシードする（テスト用）。

## Objective-C Declaration
```objective-c
- (void)_seedResourceLoadStatisticsForTestingWithFirstParty:(NSURL *)firstPartyURL thirdParty:(NSURL *)thirdPartyURL shouldScheduleNotification:(BOOL)shouldScheduleNotification completionHandler:(void(^)(void))completionHandler  WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Discussion
`seedResourceLoadStatisticsForTesting` を first/third party の `RegistrableDomain` と通知フラグで呼び、完了後に completionHandler を実行する。

## References
- [`WKProcessPoolPrivate.h#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L186)
- [`WKProcessPool.mm#L638`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L638)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
