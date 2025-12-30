# ``WKInternalsNotes/_WKMediaSessionCoordinator/delegate``

テスト用の coordinator では helper が delegate に設定される。

## Objective-C Declaration
```objective-c
@property (nullable, weak) id <_WKMediaSessionCoordinatorDelegate> delegate;
```

## Default Value
通常は `nil`。テスト用 coordinator 作成時に設定される。

## Discussion
`WKMediaSessionCoordinatorForTesting` 生成時に `WKMediaSessionCoordinatorHelper` を作成して `delegate` に設定し、delegate 呼び出しを `MediaSessionCoordinatorClient` に転送する。

## References
- [`WKWebViewPrivateForTesting.h#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L219)
- [`WKWebViewTesting.mm#L749`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L749)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
