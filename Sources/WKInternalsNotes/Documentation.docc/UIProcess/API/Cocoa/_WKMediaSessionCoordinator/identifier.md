# ``WKInternalsNotes/_WKMediaSessionCoordinator/identifier``

テスト用 coordinator ではクライアント側の `identifier` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString * _Nonnull identifier;
```

## Default Value
未調査（初期化経路の確認が必要）。

## Discussion
`WKMediaSessionCoordinatorForTesting` が `[m_clientCoordinator identifier]` の値をそのまま返す。

## References
- [`WKWebViewPrivateForTesting.h#L220`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L220)
- [`WKWebViewTesting.mm#L803`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L803)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
