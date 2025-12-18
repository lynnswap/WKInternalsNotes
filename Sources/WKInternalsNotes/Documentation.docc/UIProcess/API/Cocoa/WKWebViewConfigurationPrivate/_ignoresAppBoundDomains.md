# ``WKInternalsNotes/WKWebViewConfiguration/_ignoresAppBoundDomains``

App Bound Domains を無視

App Bound Domains によるナビゲーション制約の判定をバイパスするためのフラグ。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setIgnoresAppBoundDomains:) BOOL _ignoresAppBoundDomains WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
iOS: `NO` / macOS: `NO`（macOS は常に `NO`）

## Discussion
- この API を使わない場合: App Bound Domains のチェックは通常どおり実行されるため、（`limitsNavigationsToAppBoundDomains` が有効な場合）App Bound Domains 外への遷移は制限されうる。
- この API で `_ignoresAppBoundDomains = YES` にすると: `WebPageProxy::setIsNavigatingToAppBoundDomainAndCheckIfPermitted` がチェックをスキップして `true` を返し、許可/不許可判定をバイパスできる。
- macOS: setter が no-op のため、挙動は変わらない。

## Details
- setter は `_setIgnoresAppBoundDomains:`。
- iOS では `API::PageConfiguration` に値が保持され、`WebPageProxy` 初期化時に `m_ignoresAppBoundDomains` へ取り込まれる。
- `WKWebViewConfiguration` は通常 `WKWebView` 初期化時にコピーされるため、`WKWebView` 生成前に設定しておく前提。
- Candidate Public API: `WKWebViewConfiguration.limitsNavigationsToAppBoundDomains`（`NO` で制限自体を無効化できる。ただし API の「バイパス」と同等とは限らない）

## References
- [`WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`WKWebViewConfigurationPrivate.h#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L110)
- [`WKWebViewConfiguration.mm#L981`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L981)
- [`APIPageConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIPageConfiguration.h)
- [`WebPageProxy.cpp#L863`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp#L863)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
